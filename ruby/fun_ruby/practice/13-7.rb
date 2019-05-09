def sum_array(nums1, nums2)
  result = []
  nums1.zip(nums2) do |num1, num2|
    result << num1 + num2
  end
  result
end


p sum_array([1, 2, 3], [4, 6, 8])
