class TicketsController < ApplicationController
	
	def index
		@tickets = Ticket.all
	end

	def new

		@ticket = Ticket.new

	end

	def create
		@ticket = Ticket.new(params[:ticket])
		if @ticket.save
			redirect_to tickets_path
		else
			render :action => "new"
		end
	end

end
