class TicketsController < ApplicationController
	before_filter :authenticate
	before_filter :is_ticket_owner, only: [ :edit, :destroy, :update]
	before_filter :member_ticket, only: [:show, :new ]
	def index
		@tickets = Ticket.all
	end

	def new

		@ticket = Ticket.new

	end

	def show
		
		@ticket = Ticket.find(params[:id])
		@project = Project.find(@ticket.project_id)

	end

	def create

		@ticket = Ticket.new(params[:ticket])
		@ticket.user_id = session[:user_id]
		@ticket.project_id = params[:project_id] #fix fix fix
		@project = Project.find(@ticket.project_id)

		if @ticket.save
			redirect_to project_path(@project)
		else
			render :action => "new"
		end
	end

	def edit
		@ticket = Ticket.find(params[:id])
	end

	def update
		
		@ticket = Ticket.find(params[:id])
		
		if @ticket.update_attributes(params[:ticket])
			redirect_to project_path(@ticket.project_id)
		else
			render :action => "edit"
		end
	end

	def destroy
		@ticket = Ticket.find(params[:id])
		@ticket.destroy
		redirect_to project_path(@ticket.project_id)
	end

end
