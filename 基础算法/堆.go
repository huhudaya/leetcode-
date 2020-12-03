type Maxheap struct{
	data []int
	size int
	cap int
}

func (m *Maxheap) Swap (index1,index2 int){
	m.data[index1],m.data[index2] = m.data[index2],m.data[index1]
}

func (m *Maxheap) heapDow (index int) {
	for 2*index+1 < m.size {
		max:= index
		if m.data[2*index+1] > m.data[max] {
			max = 2*index+1
		}
		if 2*index+2 < m.size &&  m.data[2*index+2] > m.data[max]{
			max = 2*index+2
		}
		if max != index{
			m.Swap(index,max)
			index = max
		}else{
			break
		}
	}
}
func (m *Maxheap) heapfyUp (index int){
	for (index-1)/2 >=0 && m.data[(index-1)/2] < m.data[index]{
		m.Swap(index,(index-1)/2 )
		index = (index-1)/2
	}
}
func smallestK(arr []int, k int) []int {
	l := len(arr)
	if l == 0 || k == 0{
		return []int{}
	}
	m := &Maxheap{
		data : []int{},
		size : 0,
		cap  : k}

	for i:=0;i<l;i++ {
		if m.size < m.cap{
			m.data = append(m.data,arr[i])
			m.size++
			m.heapfyUp(m.size-1)
		}else{
			if arr[i] < m.data[0] {
				m.data[0] = arr[i]
				m.heapDow(0)
			}
		}
	}
	return m.data
}