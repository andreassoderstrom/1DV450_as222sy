class Project < ActiveRecord::Base
  attr_accessible :name, :description, :start_date, :end_date, :owner_id, :body

  has_many :tickets, :dependent => :destroy
  has_and_belongs_to_many :users

end
