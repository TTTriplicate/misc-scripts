#!/usr/bin/python3
'''
Written for extra credit on a Networking assignment.  
Could be easily used for any assignment involving UDP checksums
feed it the correct header information and it outputs the checksum.

Headers to feed in (in 16-bit hexadecimal words):
    Source IP
    Dest. IP
    0011
    hex(length of data in bytes)
    The entire datagram broken into 16-bit hexadecimal words

Much of this is done already by packet-siffing programs like Wireshark.
All of this data can be extracted from there.
'''

def checksumCalc(bytes):
        '''
        takes the header and psuedoheader UDP info as a list of two byte words in hexadecimal
        outputs the UDP checksum
        '''
        checksum = 0
        for i in bytes:
            checksum += int(i, 16)#sum up all the words
        while len(hex(checksum)) > 6:#handle overflow
            checksum = hex(checksum)
            overflow = str(checksum)[:len(checksum)-4]
            base = "0x" + checksum[3:]
            checksum = int(overflow, 16) + int(base, 16)

        checksum = bin(checksum)#bitwise operator didn't really work well
                                #so I did one's complement manually
        flipped = "0b"
        for b in checksum[2:]:#skip binary identifier
            if b == '0':
                flipped += "1"
            else:
                flipped += "0"
        
        return(hex(int(flipped,2)))#convert back to hex from binary

        def getWords():
            '''
            takes in a string of 2 byte hexadecimal words
            outputs a list of those words
            words should be:
            2 words for source and destination ip
            0011 for UDP
            1 word for length of UDP portion
            1 word each for source and destination port
            all of the packet data as 2 byte words, padded at the left if necessary
            '''
            bytes = []
            words = input("Enter the packet details as two byte hexadecimal words:")
            for n in words.split():
                bytes.append(hex(int(n, 16)))
            return bytes

        print(checksumCalc(getWords()))
