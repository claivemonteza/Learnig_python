import arrow

# Install Arrow
# pip install arrow

date = arrow.get('2024-08-17', 'YYYY-MM-DD')
data = date.shift(weeks=+6).format('MMM DD YYYY')
print(data)