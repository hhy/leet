package a;

/**
 * Single Number Total Accepted: 7902 Total Submissions: 17374 My Submissions
 * Given an array of integers, every element appears twice except for one. Find
 * that single one.
 * 
 * Note: Your algorithm should have a linear runtime complexity. Could you
 * implement it without using extra memory?
 * 
 * @author bart
 * 
 */

public class SingleNumber {
	public int singleNumber(int[] A) {
		int m = 0;
		for (int i = 0; i < A.length; i++) {
			m ^= A[i];
		}
		return m;
	}

	/**
	 * @param args
	 */
	public static void main(String[] args) {
		int[] a = new int[] { 5, 6, 7, 6, 5, 8, 9, 9, 8 };
		SingleNumber sn = new SingleNumber();
		System.out.println(sn.singleNumber(a));

	}

}
