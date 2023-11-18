import sentry_sdk

sentry_sdk.init(
    dsn="https://d09890daeb48aba9775c3057a28b5cb7@o4506243842572288.ingest.sentry.io/4506245309267968",
    # Set traces_sample_rate to 1.0 to capture 100%
    # of transactions for performance monitoring.
    traces_sample_rate=1.0,
    # Set profiles_sample_rate to 1.0 to profile 100%
    # of sampled transactions.
    # We recommend adjusting this value in production.
    profiles_sample_rate=1.0,
)


def hello():
    return "hello world!"


if __name__ == "__main__":
    hello()
