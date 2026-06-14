from collections import defaultdict

class TimeMap:

    def __init__(self):
        self.timemap_dct=defaultdict(dict)
    def set(self, key: str, value: str, timestamp: int) -> None:
        self.timemap_dct[key][timestamp]=value

    def get(self, key: str, timestamp: int) -> str:
        try: value = self.timemap_dct[key][timestamp] 
        # Specific timeframe not found, therefore search for a previous smaller timeframe and retrieve its value
        except: 
        # Search for the closest previous timestamp and retrieve its value
            found_closest=False
            for i in range(timestamp, 0, -1):
                print(i, self.timemap_dct)
                if i in self.timemap_dct[key]: 
                    found_closest=True
                    break
            if not found_closest: value=""
            else: value = self.timemap_dct[key][i] 
        return value