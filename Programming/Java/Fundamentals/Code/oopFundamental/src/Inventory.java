import java.util.ArrayList;

import items.Consumables;
import items.Item;
import items.MedicalSupplies;
import items.Weapons;

public class Inventory {
    private ArrayList<Item> items;

    public Inventory() {
        items = new ArrayList<>();
    }

    public ArrayList<Item> getItems() {
        return items;
    }
    
    public void addItem(Item item) {
        items.add(item);
    }

    // Example of method overloading (this is not practical in this case)
    public void addItem(String name, int quantity, int healthPointsInc) {
        items.add(new MedicalSupplies(name, quantity, healthPointsInc));
    }
    public void addItem(String name, int quantity, int damage, String type) {
        items.add(new Weapons(name, quantity, damage, type));
    }
    public void addItem(String name, int quantity, String type) {
        items.add(new Consumables(name, quantity, type));
    }


    public void displayItems() {
        for(Item item : items) {
            System.out.println(item.toString());
        }
    }
}
