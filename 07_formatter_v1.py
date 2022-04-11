symbol="*"
text="hello world"
sides=symbol *3

formatter_text=f"{sides}{text}{sides}"
top_bottom=symbol * len(formatter_text)

print(top_bottom)
print(formatter_text)
print(top_bottom)

