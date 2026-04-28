import csv

class Node:
    def __init__(self, row):
        self.id = row["id"]
        self.parent = row["parentId"]
        self.type = row["type"]
        self.text = row["text"]
        self.options = row["options"]
        self.target = row["target"]
        self.signal = row["signal"]

class ReflectionAgent:
    def __init__(self, file_path):
        self.nodes = {}
        self.children = {}
        self.state = {"answers": {}, "signals": {}}
        self.load_tree(file_path)

    def load_tree(self, file_path):
        with open(file_path, newline='', encoding="utf-8") as f:
            reader = csv.DictReader(f, delimiter="\t")
            for row in reader:
                node = Node(row)
                self.nodes[node.id] = node
                if node.parent:
                    self.children.setdefault(node.parent, []).append(node.id)

    def apply_signal(self, signal):
        if not signal:
            return
        key = signal.strip()
        self.state["signals"][key] = self.state["signals"].get(key, 0) + 1

    def get_next_from_decision(self, node, last_answer):
        rules = node.options.split(";")
        for rule in rules:
            condition, target = rule.split(":")
            condition = condition.replace("answer=", "")
            values = condition.split("|")
            if last_answer in values:
                return target
        return None

    def run(self):
        current_id = "START"
        last_answer = None

        while True:
            node = self.nodes[current_id]

            if node.type in ["start", "bridge"]:
                print("\n" + node.text)
                current_id = node.target or self.children.get(current_id, [None])[0]

            elif node.type == "question":
                print("\n" + node.text)
                options = node.options.split("|")

                for i, opt in enumerate(options):
                    print(f"{i+1}. {opt}")

                choice = int(input("Choose: ")) - 1
                answer = options[choice]
                self.state["answers"][node.id] = answer
                last_answer = answer

                self.apply_signal(node.signal)

                current_id = self.children[node.id][0]

            elif node.type == "decision":
                next_id = self.get_next_from_decision(node, last_answer)
                current_id = next_id

            elif node.type == "reflection":
                print("\n" + node.text)
                self.apply_signal(node.signal)
                input("Press Enter to continue...")
                current_id = self.children.get(node.id, [None])[0]

            elif node.type == "summary":
                print("\n--- SUMMARY ---")
                print(node.text)
                current_id = self.children.get(node.id, [None])[0]

            elif node.type == "end":
                print("\n" + node.text)
                break

            else:
                break


if __name__ == "__main__":
    agent = ReflectionAgent("../tree/reflection-tree.tsv")
    agent.run()
