package DSA_in_Java.Arrays;

import java.util.Arrays;
import java.util.HashMap;
import java.util.HashSet;
import java.util.Map;

public class Arrays_LC {
    public static void main(String[] args){
        Arrays_LC test = new Arrays_LC(); 
        // test.validAnagram("hey", "hi"); 
    }

    public static int[] twoSum(int[] nums, int target){
        // one we make a hash map:
        Map<Integer, Integer> map = new HashMap<>();
        int rem = 0; 

        // iterate through the array:
        for (int i = 0; i < nums.length; i++){
            rem = target - nums[i]; 

            if (map.containsKey(rem)){
                return new int[] {i, map.get(rem)}; 
            }

            // otherwise we have to add it to the map:
            map.put(nums[i], i); 
        }

        return new int[] {}; 
    }

    // we can also do with hashSet which is even better
    public static boolean containsDuplicate(int[] nums){
        Map<Integer, Integer> freq = new HashMap<>(); 

        for (int i = 0; i < nums.length; i++){
            if (freq.containsKey(nums[i])){
                // update the value to two:
                return true; 
            } else {
                freq.put(nums[i], 1); 
            }
        }
        return false; 
    }

    public static boolean containsDuplicateHashSet(int nums[]){
        HashSet<Integer> seenNumbers = new HashSet<>(); 

        for (int num : nums){
            if (seenNumbers.contains(num)){
                return true; 
            }
            seenNumbers.add(num); 
        }
        return false; 
    }

    public static boolean containsDuplicateTwo(int nums[], int k){
        Map<Integer, Integer> map = new HashMap<>(); 
        int j = 0; 

        for (int i = 0; i < nums.length; i++){
            if (map.containsKey(nums[i])){
                j = map.get(nums[i]); 

                if (Math.abs(i - j) <= k){
                    return true; 
                }
            }

            map.put(nums[i], i);
        }

        return false; 
    }

    public static boolean validAnagram(String s, String t){
        int[] firstString = new int[27]; 
        int[] secondString = new int[27]; 
        int asciiS = 0; 
        int asciiT = 0; 
        s = s.toLowerCase(); 
        t = t.toLowerCase(); 

        
        if (s.length() != t.length()){
            return false;
        }

        for (int i = 0; i < s.length(); i++){
            asciiS = s.charAt(i) - 'a'; 
            asciiT = t.charAt(i) - 'a'; 

            firstString[asciiS] += 1; 
            secondString[asciiT] += 1; 

        }

        return Arrays.equals(firstString, secondString);

    }
}
