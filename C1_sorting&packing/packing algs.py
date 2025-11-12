class Packing:
    """
    packets should be a list of integers, bin_size should be an integer
    pack_type specification:
    "ff" for first fit, "dec_ff" for decreasing first fit, "full_bin" for full bin packing
    default type is first fit
    """
    def __init__(self, packets, bin_size, pack_type="ff"):
        if type(packets) is not list:
            raise TypeError
        else:
            self.packets = packets
        if type(bin_size) is not int:
            raise TypeError
        else:
            self.bin_size = bin_size
        self.pack_type = pack_type
        self.bins = [[]]

        if self.pack_type == "dec_ff" or self.pack_type == "full_bin":
            self.packets = self.packets.sort(True)

        print(f"the minimum number of bins in theory is {self.theory_min()}")
        self.ff_packing()

    def theory_min(self):
        packet_sum = 0
        for packet in self.packets:
            packet_sum += packet
        return packet_sum // self.bin_size + 1

    def ff_packing(self):
        print(self.packets)
        for packet in self.packets:
            done = True
            for one_bin in self.bins:
                if sum(one_bin) + packet <= self.bin_size:
                    one_bin.append(packet)
                    print(self.bins)
                    break
                else:
                    done = False
            if not done:
                self.bins.append([packet])
                print(self.bins)
            self.packets.remove(packet)
            # print(self.packets)
        print(self.bins)


Packing([6,7,14,9,2,13], 20)
