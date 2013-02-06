class CreateProjects < ActiveRecord::Migration
  def change
    create_table :projects do |t|
      t.string "name", :limit => 50
      t.string "description", :limit => 500
      t.datetime "start_date"
      t.datetime "end_date"
      t.integer "owner_id"
      t.timestamps
    end
  end
end
