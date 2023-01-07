public class HanoiTowers {
    int numRings;
    int[] pegOne;
    int[] pegTwo;
    int[] pegThree;

    public HanoiTowers(int numRings) {
        this.numRings = numRings;
        pegOne = new int[numRings];
        pegTwo = new int[numRings];
        pegThree = new int[numRings];
        for (int i = 0; i < numRings; i++) {
            pegOne[i] = i + 1;
            pegTwo[i] = 0;
            pegThree[i] = 0;
        }
    }

    public static String playHanoi(int numRings) {
        return playHanoi(numRings, 1, 3);
    }

    public static String playHanoi(int numRings, int curr, int goal) {
        if (numRings == 1) {
            return "Move 1 from " + curr + " to " + goal + "\n";
        }
        return playHanoi(numRings - 1, curr, 6 - curr - goal) +
                "Move " + numRings + " from " + curr + " to " + goal + "\n" +
                playHanoi(numRings - 1, 6 - curr - goal, goal);
    }

    public static void main(String[] args) {
        System.out.println(playHanoi(4));
    }


}
