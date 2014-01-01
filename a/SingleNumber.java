package a;

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
