class User < ActiveRecord::Base
   attr_accessible :first_name, :last_name, :email, :password, :body
end
