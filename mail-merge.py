
## Mail Merge

# winners = list(open('mail/winners.txt', 'r'))
# print(winners)

# Opening Two files to work with...

with open('mail/message.txt', 'r') as message_file:
    message = message_file.read()

with open('mail/winners.txt', 'r') as winners_file:
    winners = winners_file.readlines()

# ... can be condensed into a short statement:
with open('mail/message.txt', 'r') as message_file, open('mail/winners.txt', 'r') as winners_file:
    message = message_file.read()
    winners = winners_file.readlines()

for winner in winners:
    filename = winner.strip('\n') + '.txt'
    with open('mail/' + filename, 'w') as f:
        f.write('Dear ' + winner.strip('\n') + ',\n') 
        f.write(message)

#print(message)
#print(winners)

