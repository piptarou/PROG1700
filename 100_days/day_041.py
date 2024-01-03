if __name__ == "__main__":
    print("Website Ratings")
    print()
    website = {"name": input("Website name? "),
            "url": input("Website url? "),
            "description": input("Website description? "),
            "rating": input("Website rating out of 5? ")
            }
    print()
    for name, value in website.items():
        print(f"{name}: {value}")