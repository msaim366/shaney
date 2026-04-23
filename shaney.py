import os, sys, random

def build(contexts, words, n):
    for i in range(len(words) - n):
        key = tuple(words[i:i+n])
        nxt = words[i+n]
        contexts.setdefault(key, {})
        contexts[key][nxt] = contexts[key].get(nxt, 0) + 1

def choose(wordfreq):
    total = sum(wordfreq.values())
    r = random.randint(1, total)
    s = 0
    for word, count in wordfreq.items():
        s += count
        if r <= s:
            return word

def generate(contexts, starters, n):
    context = random.choice(starters)
    output = list(context)

    while tuple(context) in contexts:
        word = choose(contexts[tuple(context)])
        output.append(word)
        context = context[1:] + [word]

    return " ".join(output)

def main():
    data_dir = sys.argv[1] if len(sys.argv) > 1 else "data/"
    n = int(sys.argv[2]) if len(sys.argv) > 2 else 2

    contexts, starters = {}, []

    for file in os.listdir(data_dir):
        with open(os.path.join(data_dir, file), encoding="utf-8") as f:
            words = f.read().split()
            if len(words) < n: continue
            starters.append(words[:n])
            build(contexts, words, n)

    text = generate(contexts, starters, n)

    with open("output.txt", "w") as f:
        f.write(text)
    print("✅ Done. Output written to output.txt")

if __name__ == "__main__":
    main()

