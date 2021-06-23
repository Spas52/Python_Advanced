nums = tuple([float(el) for el in input(). split()])

result = {}

for num in nums:
    if num not in result:
        result[num] = 0
    result[num] += 1

sorted_result = sorted(result.items(), key=lambda x: x[0])
# ot nai malkoto kam nai-golqmoto sortirano po key
# sorted_result = sorted(result.items(), key=lambda x: x[1])
# sashtoto kato gornoto no e sortirano po value
# a ako iskame descending da stane prosto slagame reverse=True taka
# sorted_result = sorted(result.items(), key=lambda x: x[0], reverse=True)
# ili moje taka x: -x[0 ili 1] not key ili value trqbva da e chislo inache nqma da stane

for key, value in result.items():
    print(f"{key} - {value} times")

