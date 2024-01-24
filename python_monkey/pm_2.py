import pythonmonkey as pm

fn_reverseAllWords = """
function reverseAllWords(str) {
  return str.split(' ').reverse().join(' ')
}
"""
pm.eval(fn_reverseAllWords)
phrase = 'The quick brown fox jumps over the lazy dog'

print(f'{phrase = }')
print(f'reverseAllWords(phrase) = {pm.globalThis.reverseAllWords(phrase)}')
print(" ".join(phrase.split(" ")[::-1]))
