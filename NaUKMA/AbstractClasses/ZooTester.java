/**
 * Test with:
 * java -ea -classpath ./out/production/third homework.ZooTester
 * */
public class ZooTester {
    /**
     * Main zoo tester method
     * TODO: replace with JUnit later on
     * */
    public static void main(String[] args) {
        testGeneral();
        testSpecific();
    }

    /**
     * General animal's check
     * */
    private static void testGeneral() {
        Lion lion = new Lion();

        // default check
        assert !lion.happy;
        assert !lion.tired;

        // "atomic" actions check
        Zookeeper.feedAnimal(lion);
        assert lion.happy;
        Zookeeper.punchAnimal(lion);
        assert !lion.happy;
        Zookeeper.feedAnimal(lion);  // so we could play with lion

        // check now lion can play
        boolean areNoExceptions = true;
        try {
            Zookeeper.playWithAnimal(lion);
        } catch (Exception e) {
            areNoExceptions = false;
        }
        assert areNoExceptions;

        // check currently lion cannot play because of tiredness
        boolean cannotPlayOfTiredness = false;
        try {
            Zookeeper.playWithAnimal(lion);
        } catch (TiredException e) {
            cannotPlayOfTiredness = true;
        } catch (BadMoodException ignored) {}
        assert cannotPlayOfTiredness;

        // to make him sad, not tired
        Zookeeper.giveRestToAnimal(lion);
        Zookeeper.punchAnimal(lion);

        // check sad, not tired
        boolean cannotPlayOfSadness = false;
        try {
            Zookeeper.playWithAnimal(lion);
        } catch (BadMoodException e) {
            cannotPlayOfSadness = true;
        } catch (TiredException ignored) {}
        assert cannotPlayOfSadness;
    }

    /**
     * Specific tests, different for each animal
     * */
    private static void testSpecific() {
        Bird bird = new Bird();
        assert Zookeeper.hearAnimalSound(bird).equals("ko-ko-ko");

        Lion lion = new Lion();
        assert Zookeeper.hearAnimalSound(lion).equals("r-r-r");
    }
}
