/**
 * Animal abstract implementation
 * */
abstract class Animal {
    public boolean happy = false;
    public boolean tired = false;

    /**
     * Animal's sound, to be over-ridden
     * */
    abstract String saySound();

    void feed() {
        happy = true;
    }

    void rest() {
        tired = false;
    }

    void punch() {
        happy = false;
    }

    private boolean isWantsToPlay() {
        return happy;
    }

    private boolean hasEnergyToPlay() {
        return !tired;
    }

    void play() throws BadMoodException, TiredException {
        if (!isWantsToPlay()) {
            throw new BadMoodException();
        }
        if (!hasEnergyToPlay()) {
            throw new TiredException();
        }

        tired = true;
    }
}

class BadMoodException extends Exception {
}

class TiredException extends Exception {
}
