#!/usr/bin/env python3
import iptoolsjj
#import iptoolsjj.iptoolsjj

print('------------------------------------------------------------------------')
print("192.168.10.10 is in 92.168.10.0/22 ?: ")
if iptoolsjj.is_in_subnet('192.168.10.10', '192.168.10.0/22'):
	print ('yes')
print('------------------------------------------------------------------------')
print("Is 192.168.1.22 valid ip ?: ")
print(iptoolsjj.verify('192.168.1.22'))
print('------------------------------------------------------------------------')
print("Is 192.168.1.22/25 valid ip/mask ?: ")
print(iptoolsjj.verify('192.168.1.22/25','ip/mask'))
print('------------------------------------------------------------------------')
print("Is 300.168.1.22/25 valid ip/mask ?: ")
print(iptoolsjj.verify('300.168.1.22/25','ip/mask'))
print('------------------------------------------------------------------------')
print("Is 192.168.1.22/255.255.255.128 valid ip/mask (x.x.x.x mask format) ?: ")
print(iptoolsjj.verify('192.168.1.22/255.255.255.128','ip/mask255'))
print('------------------------------------------------------------------------')
print("Subnet ip for 191.123.1.36/27 ?: ")
print(iptoolsjj.get_subnet_ip('191.123.1.36/27'))
print('------------------------------------------------------------------------')
print("Convert mask 255.255.255.240 to prefix?: ")
print(iptoolsjj.mask255_to_dec('255.255.255.240'))
print('------------------------------------------------------------------------')
print("Convert prefix 28 to mask x.x.x.x ? (list,string): ")
print(iptoolsjj.dec_to_mask255(28))
print(iptoolsjj.dec_to_mask255(28,output='string'))



