class DiningPhilosophers {

    private Semaphore[] forks = new Semaphore[5];
    
    public DiningPhilosophers() {
        for(int i = 0; i < 5; i++) {
            forks[i] = new Semaphore(1);
        }
    }

    // call the run() method of any runnable to execute its code
    public void wantsToEat(int philosopher,
                           Runnable pickLeftFork,
                           Runnable pickRightFork,
                           Runnable eat,
                           Runnable putLeftFork,
                           Runnable putRightFork) throws InterruptedException {
        
        Semaphore rightFork = forks[philosopher];
        Semaphore leftFork = forks[(philosopher + 1) % 5];
        
        rightFork.acquire();
        pickRightFork.run();
        
        leftFork.acquire();
        pickLeftFork.run();
        
        eat.run();
        
        putLeftFork.run();
        leftFork.release();
        
        putRightFork.run();
        rightFork.release();
    }
}