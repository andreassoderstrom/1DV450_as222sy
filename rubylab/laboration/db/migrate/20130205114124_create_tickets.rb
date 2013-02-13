class CreateTickets < ActiveRecord::Migration
  def change
    create_table :tickets do |t|

      t.references :user, :project, :status

      t.string "name", :limit => 50
      t.string "description", :limit => 500
      t.timestamps
    end
  end
end
