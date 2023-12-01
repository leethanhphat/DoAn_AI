class Item:
    
    def __init__(self, name, weight, value):
        self._name = name  
        self._weight = weight  
        self._value = value  

    def get_name(self):
        return self._name  

    def set_name(self, name):
        self._name = name  

    def get_weight(self):
        return self._weight  

    def set_weight(self, weight):
        self._weight = weight  

    def get_value(self):
        return self._value  

    def set_value(self, value): 
        self._value = value  

#để tính tỷ lệ giá trị trên cân nặng của món hàng, tức là giá trị chia cho trọng lượng.+
    def unitPrice(self):
        return self._value / self._weight

class Greedy:
    # sắp sếp độ ưu tiên chọn các món hàng có unitPrice(đơn giá) giảm dần theo thuật toán Selection Sort. Mục đích là để chọn các món hàng có đơn giá cao trước.
    def sort(self, items):
        n = len(items)
        for i in range(n):
            max_idx = i
            for j in range(i+1, n):
                if items[j].unitPrice() > items[max_idx].unitPrice():
                    max_idx = j
            temp = items[i]
            items[i] = items[max_idx]
            items[max_idx] = temp

    #Phương thức này thực hiện việc chọn các món hàng để đặt vào balo với giới hạn trọng lượng capacity.
    #Nó lặp qua danh sách các món hàng đã được sắp xếp và thêm chúng vào balo cho đến khi không còn khả năng đặt thêm món hàng nào hoặc balo đầy
    def Knapsack(self, items, capacity):
        total_value = 0    # Tổng giá trị lấy được
        list_result = []    # các món hàng đã lấy

        for item in items:
            #chọn các món hàng có đơn giá cao trước
                # chọn các món hàng được ưu tiên cho đến khi đạt giới hạn
            if capacity >= item.get_weight():

                list_result.append(item)
                total_value += item.get_value()
                capacity -= item.get_weight()

        return total_value, list_result

#Danh =sach chưa' cac' mon' hàng
listItem = []

#tạo đối tương Greedy để gọi các phương thức của class này
gd = Greedy()


item1 = Item("A", 2, 50) 
item2 = Item("B", 8, 200)
item3 = Item("C", 3, 120)
item4 = Item("D", 5, 190)
item5 = Item("E", 1, 20)


listItem.append(item1)
listItem.append(item2)
listItem.append(item3)
listItem.append(item4)
listItem.append(item5)
            
gd.sort(listItem)

#=sưc' chưa' balo
capacity = 10
# lấy kết quả Tổng giá trị lấy được và list những món hàng đã lấy với capacity = 10 
total_value, select_items = gd.Knapsack(listItem, capacity)


print("Selected Items:")
for item in select_items:
     print(f"{item.get_name()} - Đơn giá: {item.unitPrice()}")

print("Tổng số lượng tất cả sản phẩm sau Knapsack", total_value)

