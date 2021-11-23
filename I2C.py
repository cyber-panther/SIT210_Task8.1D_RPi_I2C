import smbus
import time

BH1750 = 0x23

reciever = 0x23

bus = smbus.SMBus(1)

def Light():
    address = bus.read_i2c_block_data(BH1750,reciever)
    value = (address[1] + (256 * address[0]))
    return value

def main():
    while True:
        light_value =Light()

        if(light_value >= 900):
            print(str(light_value) + " -> Too Bright")
            
        elif(light_value > 500 and light_value < 900):
            print(str(light_value) + " -> Bright")
            
        elif(light_value > 100 and light_value < 500):
            print(str(light_value) + " -> Medium")
            
        elif(light_value < 100 and light_value > 20):
            print(str(light_value) + " -> Dark")
            
        else:
            print(str(light_value)+" -> Too Dark")
     
        time.sleep(1)

main()
