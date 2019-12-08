def dedupe(items):
    seen = set()
    for item in items:
        if item not in seen:
            yield item
            seen.add(item)

nums = [1,1,1,3,3,4,4,3,5,4,3,1,2]
uniques = dedupe(nums)
print(list(uniques))