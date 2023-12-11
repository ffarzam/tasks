class MyDataFrame:
    def __init__(self, data, columns):
        self.data = data
        self.columns = columns

    def __str__(self):
        rows = []
        for row in self.data:
            formatted_row = [str(val) if val is not None else "None" for val in row]
            rows.append("\t".join(formatted_row))
        header = "\t".join(map(str, self.columns))
        n = '\n'
        return f"{header}\n{n.join(rows)}"

    def __getitem__(self, key):
        if isinstance(key, str) and key in self.columns:
            return [item[self.columns.index(key)] for item in self.data]
        elif isinstance(key, list):
            return [[item[self.columns.index(i)] for item in self.data] for i in key]

    def __getattr__(self, key):
        if key in self.columns:
            return [item[self.columns.index(key)] for item in self.data]
        else:
            raise AttributeError(f"'MyDataFrame' object has no attribute '{key}'")

    def index(self, row_num):
        return list(self.data[row_num])

    def sort(self, column, mode="ascending"):
        def sort_key(item):
            value = self.data[self.columns.index(column)][item]
            return value if value is not None else float('-inf')

        flag = mode != "descending"
        sorted_indices = sorted(range(len(self.data[self.columns.index(column)])), key=sort_key, reverse=flag)
        sorted_data = [self.data[i] for i in sorted_indices]
        return MyDataFrame(sorted_data, columns=self.columns)


# Example usage
df = MyDataFrame([(1, 2, 3), (4, None, 10), (5, 1, 19)], columns=["a", "b", "c"])

print(df)
print(df.a)
print(df["a"])
print(df[["a", "c"]])
print(df.index(1))
print(df.sort("b", mode="ascending"))
