# Check for Proth number using Python

def PowerOfTwo(n):     

    return (n and (not(n & (n - 1))))   

    
      
# Function to check if the given number is Proth number or not 

def isProthNumber( n): 

    k = 1
    while(k < (n//k)):   

        # check if k divides n or not 

        if(n % k == 0): 

  

            # Check if n / k is power of 2 or not 

            if(PowerOfTwo(n//k)): 

                    return True

        # update k to next odd number 

        k = k + 2       

   

    return False

          

              

              
# Testing the code
  
# Get n 

n = 41; 

  
# Check n for Proth Number 

if(isProthNumber(n-1)): 

    print("YES"); 

else: 

    print("NO"); 