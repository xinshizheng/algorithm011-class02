class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = {}
        for item in strs:
            key = tuple(sorted(item))
            hashmap[key] = hashmap.get(key, []) + [item]
        return list(hashmap.values())
