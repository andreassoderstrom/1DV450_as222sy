class CreateTickets < ActiveRecord::Migration
  def change
    create_table :tickets do |t|

      t.references :users, :projects, :statuses

      t.string "name", :limit => 50
      t.string "description", :limit => 500
      t.timestamps
    end
  end
end
