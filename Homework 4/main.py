def example1():
    for i in range( 3 ):
        try:
            x = int( input( "enter your first number: " ) )
            y = int( input( "enter your second number: " ) )
            print( x, '/', y, '=', x/y )
        except:
            print('Error, Please only input numbers "ex. 1, 2, 3, 4"')

def example2( L ):
    print( "\n\nExample 2" )
    sum = 0
    sumOfPairs = []
    for i in range( len( L ) ):
        sumOfPairs.append( L[i]+L[i+1] )

    print( "sumOfPairs = ", sumOfPairs )


def printUpperFile( fileName ):
   file = open( fileName, "r" )
   for line in file:
       print( line.upper() )
   file.close()
    
def main():
    example1()
    L = [ 10, 3, 5, 6, 9, 3 ]
    example2( L )
    example2( [ 10, 3, 5, 6, "NA", 3 ] )
    example3( [ 10, 3, 5, 6 ] )

    printUpperFile( "doesNotExistYest.txt" )
    printUpperFile( "./Dessssktop/misspelled.txt" )

main()
