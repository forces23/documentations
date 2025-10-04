package player;

import items.Item;

public abstract class Player implements PlayerInterface {
    private String name;
    private int healthPoints;
    private int level;
    private Item[] inventory;

    // Constructor
    public Player(String name, int healthPoints, int level, Item[] inventory) {
        this.name = name;
        this.healthPoints = healthPoints;
        this.level = level;
        this.inventory = inventory;
    }

    // NAME getter and setter 
    @Override
    public String getName() {
        return name;
    }
    @Override
    public void setName(String name) {
        this.name = name;
    }

    // HEALTHPOINTS getter and setter 
    @Override
    public int getHealthPoints() {
        return healthPoints;
    }
    @Override
    public void setHealthPoints(int healthPoints) {
        this.healthPoints = healthPoints;
    }

    // LEVEL getter and setter 
    @Override
    public int getLevel() {
        return level;
    }
    @Override
    public void setLevel(int level) {
        this.level = level;
    }

    // INVENTORY getter and setter 
    @Override
    public Item[] getInventory() {
        return inventory;
    }
    @Override
    public void setInventory(Item[] inventory) {
        this.inventory = inventory;
    }
    

    public abstract void displayPlayerInfo();

}
