class Solotion:
    def min_num_of_steps(self,num_of_nums,n):
        result=0
        nums = n.split(" ")
        m=max(nums)
        max_idx=[]
        for i,num in enumerate(nums):
            if num==m:
                max_idx.append(i)

        if 0 not in max_idx:
            max_idx.insert(0,0)
        if int(num_of_nums)-1 not in max_idx:
            max_idx.append(int(num_of_nums)-1)

        for i in range(len(max_idx)-1):
            result+=int(m)-int(min(nums[int(max_idx[i]):int(max_idx[i+1]+1)]))
            return result
        
if __name__ == '__main__':
    p1=Solotion()
    print(p1.min_num_of_steps('3','1 3 2'))
