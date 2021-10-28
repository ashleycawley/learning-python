#!/usr/bin/env python3

guest = "Frankie" # My variable

# if something is in a list:

# NOTE: The BAD repetitive way:
if guest == "Frankie" or guest == "Ryan" or guest == "Claire" or guest == "Phil":
    print("Yay! Friend.")


# NOTE: Better Way:
guest_list = ["Frankie", "Ryan", "Claire", "Phil"]
if guest in guest_list:     # NOTE: "if" and "in" being the important part
    print("Yay! Friend.")