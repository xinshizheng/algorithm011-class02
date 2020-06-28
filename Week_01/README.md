学习笔记

### Array
数组是有序的元素序列，在内存中元素存储在连续的地址。
prepend, append, lookup（O(1)）
insert, delete（O(n)）

Python:
```
array_list = [] # 新建
array_list[i] # 查询第i个元素
array_list.insert(idx, obj) # 在idx位置上插入元素obj
array_list.append(obj) # 在数组末尾添加元素obj
array_list.pop(idx) # 删除idx位置的元素
```

### Linked List, Skip List
链表适用于需要频繁插入删除元素的场景，各元素不需连续的内存地址进行存储，通过next指针指向下一个节点。包括单链表(next)、双链表(prev+next)、循环链表(tail->head)等
lookup（O(n)）
prepend, append, insert, delete（O(1))

跳表：通过添加索引加速有序链表的查询(插入、删除、搜都是O(log(n)))。优势：原理简单、容易实现、方便拓展、效率更高，对标平衡树和二分查找。空间复杂度O(n)
经验：通过增加维度（e.g.一维数据结构->二维），空间换时间


### Stack, Queue, Priority Queue, Double-ended Queue
栈：Last In First Out (添加、删除O(1))
队列：First In First Out (添加、删除O(1))
查询复杂度O(n)，因为无序需要遍历

实战中使用Double-ended Queue（Deque）：Queue与Stack结合体。可从两端进行元素的出入。插入和删除O(1)，查询O(n)
Python: collections.deque

优先队列：插入(O(1))，取出(O(log(n))):按元素优先级取出
底层具体实现的数据结构较为多样和复杂，可以用heap、bst、treap
Python: heapq