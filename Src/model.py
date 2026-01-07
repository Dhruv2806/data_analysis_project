from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

def train_model(df):
    df['Day'] = df['Date'].dt.day

    X = df[['Day', 'Price']]
    y = df['Revenue']

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    model = LinearRegression()
    model.fit(X_train, y_train)

    score = model.score(X_test, y_test)
    print(f"\nModel R² Score: {score:.2f}")

    return model
