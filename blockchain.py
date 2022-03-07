




Mining_Reward = 10


genesis_block = {   "previous_hash" : "", 
                    "index_no." : 0, 
                    "transaction" : [] 
                }

blockchain = []
blockchain.append(genesis_block)
open_transactions = []
tx = []

owner = " Saksham "
participants = 'Saksham'


def hash_block(block):
    return "-".join([str(block[keys]) for keys in block])


# a function to let user input the initial value and update the last transaction that happened on the chain.
def get_last_blockchain_value():
    updated_last_value  = blockchain[-1] 

    return updated_last_value


def get_balance (participants):
    # calculates the balance, i.e. if the participant has enough money to spend in his wallet
    ''' in the list comprehension, we are geting the amount for a given transaction for all transactions in a block if the sender of that transaction is the participant for all blocks in the blockchain '''
    
    # tx_sender = [[tx['amount'] for tx in block['transaction'] if tx['sender'] == participants ]for block in blockchain]
    open_tx_sender= [[tx['amount'] for tx in open_transactions if tx['sender'] == participants]]
   
    # amount_sent = 0
    # for tx in tx_sender:
    #      if len(tx) >= 0:
    #         amount_sent = tx[0] - amount_sent 
   
    tx_recipient = [[tx['amount'] for tx in block['transaction'] if tx['recipient'] == participants ]for block in blockchain]
    tx_recipient.append(open_tx_sender)
    amount_recieved = 0
    for tx in tx_recipient:
        if len(tx) > 0:
                amount_recieved = str(amount_recieved) + str(tx[0])
    return  amount_recieved 

def verify_transaction(transaction):
    sender_balance = get_balance(transaction['sender'])
    return sender_balance >= str(transaction['amount'])
        


def get_transaction_data(  recipient, sender = owner , amount = 1.0 ): 

    ''' sender = sender of the transaction 
        recipient = recipient of the transaction 
        amount = ampunt of the transaction
    '''
    transaction = { "sender" : sender, "recipient" : recipient, "amount" : amount }
   
    if verify_transaction(transaction) :
        open_transactions.append(transaction)
        participants.add(sender)
        participants.add(recipient)
        return True 
       
    file = open_transactions

    print ('your transaction value has been added succefully and here is the whole blockchain data  : ', file )
    print( " -_- " * 10 )
    




def mine_block ():
# a function to create more new blocks in the blockchain
    ''' the idea behind this function is when it is called all open transactions are taken and added to a block which then is added to the blockhain
        here the transaction : open_transaction variable depicts the height of the blockchain
    '''
    last_block = blockchain[-1]
    hashed_block = hash_block(last_block)
  
    reward_transaction = {'sender': 'MINING', 'amount': Mining_Reward, 'recipient' : owner }
    copied_transaction = open_transactions[:]
    copied_transaction.append (reward_transaction)
    block = {"previous_hash" : hashed_block, "index_no." : len(blockchain), "transaction" : open_transactions} 

    # for keys in block:
    #     value = last_block[keys]
    #     hashed_block = hashed_block + str(value)
    blockchain.append(block)
    
    return True




def get_user_input ():
     
     tx_amount = float (input ( 'please enter the transaction amount : '))
     tx_recipient = input (" please enter the recipient's address : ")
     return  (tx_recipient, tx_amount)





def get_user_choice():
    choice = input(" please make a choice :  ")
    return choice





def ouput_block_individually():
    # outout the blocks individually
        for block in blockchain:
            print ("outputing block individually")
            print (block)
        print( "--" * 50 )    






def verify_blockchain():
    # verfies the that there is no manupilation in the blocks. it compares the hash of the previous block along with hashing the previuos block. if the hash matches then it return true otherwise false 
    for (index, block) in enumerate(blockchain):
        if index == 0:
            continue 
        if block['previous_hash'] != hash_block(blockchain[index-1]):
            return False
    return True
 






waiting_for_input = True      
while waiting_for_input == True:

    print (" please choose an option ")
    print (" 1 : if you want to add a transaction")
    print (" 2 : if you want to get the blockchain list")
    print (" 3 : mine block")
    print (" 4 : to know about the participants involved")
    print (" Q : if you want to quit the loop ")
    print (" H : manipulate  ")
    user_choice = get_user_choice()

    if user_choice == "1":
        transaction_data = get_user_input()
        recipient, amount = transaction_data # this will extract the data fom the tuple created in the get_user_input function
        get_transaction_data(recipient, amount= amount)
        #print ( open_transactions )
        
    elif user_choice == "2":
# output the blocks individually
        all_individual_blocks = ouput_block_individually()

    elif user_choice == "3":
        if mine_block():
            open_transactions = []

    elif user_choice == "4":
        print (participants)
    
    
    elif user_choice == "h" or "H":
        if len(blockchain) >= 1:
            blockchain[0] = {   "previous_hash" : "", 
                    "index_no." : 0, 
                    "transaction" : [{'sender' : 'chris', 'recipient' : 'max_address', 'amount' : " 000 "}] 
                }

            

    elif user_choice == "Q" or "q":
         waiting_for_input = False

   

    else:
        print (" invalid user input, please choose form the given options ")
    
    if verify_blockchain() == False :
        print ("invalid blockchain") 
        break 

    print (get_balance('Saksham'))
    

print (" you tried to manipulate me and hence am done with you ")



        




