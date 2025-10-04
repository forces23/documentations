package items;
public class Item {
    private String name;
    private int quantity;
    private String itemClass = "Misc";

    // Build the constructor for item class
    public Item(String name, int quantity) {
        this.name = name;
        this.quantity = quantity;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public int getQuantity() {
        return quantity;
    }

    public void setQuantity(int quantity) {
        this.quantity = quantity;
    }

    @Override
    public String toString() {
        return "Category: " + itemClass + ", Item: " + name + ", Quantity: " + quantity;
    }


}
