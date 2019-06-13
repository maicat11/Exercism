
class Darts {
    private double z;

    Darts(double x, double y) {
        z = Math.sqrt(x*x + y*y);
    }

    int score() {
        if (z <= 1) {
            return 10;
        }
        if (z <= 5) {
            return 5;
        }
        if (z <= 10) {
            return 1;
        }
        return 0;
    }
}
