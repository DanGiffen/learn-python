bidder_dic = {}
auction_list=[]
other_bidder = "yes"
while other_bidder == "yes":
    print("Welcome to the silent auction\n")
    name = input("What's your name?\n")
    bid = input("What's your bid?\n")
    bidder_dic["name"] = name
    bidder_dic["bid"] = bid
    auction_list.append(bidder_dic)
    other_bidder = input("Are there any other bidders? yes or no\n").lower()
    print(auction_list)