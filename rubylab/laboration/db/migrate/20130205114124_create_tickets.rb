class CreateTickets < ActiveRecord::Migration
  def change
    create_table :tickets do |t|

      t.references :users, :projects, :statuses

      t.string "name", :limit => 50
      t.string "description", :limit => 500
      t.integer "project_id"
      t.integer "status_id"
      t.integer "owner_id"
      t.timestamps
    end
  end
end
