package items;
public class Consumables extends Item {
    private String type;
    private String itemClass = "Consumables";

    public Consumables( String name, int quantity, String type) {
        super(name, quantity); // super is used to call the parent class constructor
        this.type = type;
    }

    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }

    public String getItemClass() {
        return itemClass;
    }

    @Override
    public String toString() {
        return "Category: " + itemClass + ", Item: " + getName() + ", Quantity: " + getQuantity() + ", Type: " + type;
    }
    
}
