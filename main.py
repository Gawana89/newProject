class convertTemp:
    count = 0
    @staticmethod
    def f_to_c(temp):
        convertTemp.count += 1
        return (temp-32)/1.8
    @staticmethod
    def c_to_f(temp):
        convertTemp.count += 1
        return (temp * 1.8) + 32
    
    @staticmethod
    def get_count_op():
        return convertTemp.count

convert = convertTemp()