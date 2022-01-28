/**
 * Zookeeper's actions towards animals
 * */
public class Zookeeper {
    public static String hearAnimalSound(Animal animal) {
        return animal.saySound();
    }

    public static void feedAnimal(Animal animal) {
        animal.feed();
    }

    public static void giveRestToAnimal(Animal animal) {
        animal.rest();
    }

    public static void punchAnimal(Animal animal) {
        animal.punch();
    }

    public static void playWithAnimal(Animal animal) throws BadMoodException, TiredException {
        animal.play();
    }
}
