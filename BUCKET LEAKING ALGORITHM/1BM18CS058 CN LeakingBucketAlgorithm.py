def main():
    bucket_size = int(input("Enter the Bucket_size"))
    
    bucket_output = int(input("Enter the size of the bucket_output"))
    n = int(input("Enter the size of the number of time you want the dta to pass"))
    for x in range(0,n):
        data_size = int(input("Enter thr size of the input only"))
        if(data_size > bucket_size):
            print("THe size has exceeded the bucket size and hence not possible to pass through it")
            return
        sent_byte = data_size%bucket_output
        print("Bucket output sucessful/nlast bytes sent are:",sent_byte,"\n")
        
main()
        
         
        
        