// homepage functionality
const menu = document.querySelector('#mobile_menu')
const menuLinks = document.querySelector('.navbar_menu')
const navLogo = document.querySelector('#navbar_logo')

//diplay mobile menu
const mobileMenu = () =>{
    menu.classList.toggle('is-active')
    menuLinks.classList.toggle('active')
}

menu.addEventListener('click', mobileMenu)

// showactive menu when scrolling
const highLightMenu = () =>{
    const elem = document.querySelector('.highlight')
    const OverviewMenu = document.querySelector('#overview-page')
    const goalMenu = document.querySelector('#goals-page')
    const incomeMenu = document.querySelector('#income-page')
    let scrollPos = window.scrollY


    // adds higlight class to my menu items
    if (window.innerWidth > 960 && scrollPos< 600){
        OverviewMenu.classList.add('highlight')
        goalMenu.classList.remove('highlight')
        return
    } 
    else if (window.innerWidth > 960 && scrollPos< 1400){
        goalMenu.classList.add('highlight')
        OverviewMenu.classList.remove('highlight')
        incomeMenu.classList.remove('highlight')
        return
    }
    else if (window.innerWidth > 960 && scrollPos< 2345){
        incomeMenu.classList.add('highlight')
        goalMenu.classList.remove('highlight')        
        return
    }

    if (elem && window.innerWidth < 960 && scrollPos < 600 || elem){
        elem.classList.remove('highlight')
    }
}

window.addEventListener('scroll', highLightMenu)
window.addEventListener('click', highLightMenu)

//close mobile menu when clicking on a new menu item
const hideMobileMenu = () => {
    const menuBars = document.querySelector(".is-active")
    if (window.innerWidth <= 768 && menuBars){
        menu.classList.toggle('is-active')
        menuLinks.classList.remove('active')
    }
}

menuLinks.addEventListener('click', hideMobileMenu)
navLogo.addEventListener('click', hideMobileMenu)
// =======================================================================================================================================
// Goals
let goals = [{
    name: 'Mortage',
    account: 'Savings',
    goaldate: '2021-10-04',
    id: '1'},
    {name: 'Loans',
    account: 'Chequeing',
    goaldate: '2021-10-04',
    id: '2'},
    {name: 'Laptop',
    account: 'Savings',
    goaldate: '2021-10-04',
    id: '3'},
    {name: 'Grocery',
    account: 'Savings',
    goaldate: '2021-10-04',
    id: '4'}]


// Deletes to do
function removeGoal(idToDelete) {
    // if filter create copy of array. Need to reassign. todo is string
    goals = goals.filter(goal => {
    //if id of this todo matches idToDelete return false and delete it otherwise leave it
        if (goal.id === idToDelete){
            return false
        } else {return true}
    })
}

 //controller
function addGoal(){
    const name = document.getElementById("gname").value
    const account = document.getElementById("gaccount").value
    const duedate = document.getElementById('gdate').value
    console.log(account)
    createGoal(name,account,duedate)
    goalRender()
}

function deleteGoal(event){
    const deleteButton = event.target;
    const idToDelete = deleteButton.id
    removeGoal(idToDelete)
    goalRender()
}


//creates to do
function createGoal(Name,Account,Duedate){
    const id = ''+ new Date().getTime() 

    goals.push({name:Name,
    account: Account,
    goaldate: Duedate,
    id: id}) 
}

 // View
function goalRender(){
    // reset list
    document.getElementById('goal-list').innerHTML = '' 

    goals.forEach(goal => {
        const element = document.createElement('div')

        element.innerText = goal.name + '  ----  ' + goal.account +'  ------  ' + goal.goaldate

        // add delete button for each element
        const deleteButton = document.createElement('button')
        deleteButton.innerText = 'Delete'
        deleteButton.style = 'margin-left: 16px'
        deleteButton.onclick = deleteGoal
        deleteButton.id = goal.id
        element.appendChild(deleteButton)
        
        const goallist = document.getElementById('goal-list')
        goallist.appendChild(element)
    });
} 
goalRender()
// =================================================================================================
// Income
let incomes = []


// Deletes to do
function removeIncome(idToDelete) {
    // if filter create copy of array. Need to reassign. todo is string
    incomes = incomes.filter(income => {
    //if id of this todo matches idToDelete return false and delete it otherwise leave it
        if (income.id === idToDelete){
            return false
        } else {return true}
    })
}

 //controller
function addIncome(){
    const name = document.getElementById("iname").value
    const account = document.getElementById("iaccount").value
    const amount = document.getElementById("iamount").value
    const duedate = document.getElementById('idate').value
    createIncome(name,account,duedate,amount)
    incomeRender()
}

function deleteIncome(event){
    const deleteButton = event.target;
    const idToDelete = deleteButton.id
    removeIncome(idToDelete)
    incomeRender()
}


//creates to do
function createIncome(Name,Account,Duedate, Amount){
    const id = ''+ new Date().getTime() 

    incomes.push({name:Name,
    account: Account,
    incomeDate: Duedate,
    iamount: Amount,
    id: id}) 
}

 // View
function incomeRender(){
    // reset list
    document.getElementById('income-list').innerHTML = '' 

    incomes.forEach(income => {
        const element = document.createElement('div')

        element.innerText = income.name + '  ----  ' + income.account +'  ------  ' + income.incomeDate + '-----'+ income.iamount

        // add delete button for each element
        const deleteButton = document.createElement('button')
        deleteButton.innerText = 'Delete'
        deleteButton.style = 'margin-left: 16px'
        deleteButton.onclick = deleteIncome
        deleteButton.id = income.id
        element.appendChild(deleteButton)
        
        const incomelist = document.getElementById('income-list')
        incomelist.appendChild(element)
    });
} 
incomeRender()
// =================================================================================================

// Expenses
let expenses = []


// Deletes to do
function removeExpense(idToDelete) {
    // if filter create copy of array. Need to reassign. todo is string
    expenses = expenses.filter(expense => {
    //if id of this todo matches idToDelete return false and delete it otherwise leave it
        if (expense.id === idToDelete){
            return false
        } else {return true}
    })
}

 //controller
function addExpense(){
    const name = document.getElementById("ename").value
    const account = document.getElementById("eaccount").value
    const amount = document.getElementById("eamount").value
    const duedate = document.getElementById('edate').value
    createExpense(name,account,duedate,amount)
    expenseRender()
}

function deleteExpense(event){
    const deleteButton = event.target;
    const idToDelete = deleteButton.id
    removeExpense(idToDelete)
    expenseRender()
}


//creates to do
function createExpense(Name,Account,Duedate, Amount){
    const id = ''+ new Date().getTime() 

    expenses.push({name:Name,
    account: Account,
    incomeDate: Duedate,
    eamount: Amount,
    id: id}) 
}

 // View
function expenseRender(){
    // reset list
    document.getElementById('expenses-list').innerHTML = '' 

    expenses.forEach(expense => {
        const element = document.createElement('div')

        element.innerText = expense.name + '  ----  ' + expense.account +'  ------  ' + expense.incomeDate + '-----'+ expense.eamount

        // add delete button for each element
        const deleteButton = document.createElement('button')
        deleteButton.innerText = 'Delete'
        deleteButton.style = 'margin-left: 16px'
        deleteButton.onclick = deleteExpense
        deleteButton.id = expense.id
        element.appendChild(deleteButton)
        
        const expenselist = document.getElementById('expenses-list')
        expenselist.appendChild(element)
    });
} 
expenseRender()
// =================================================================================================

// Investments
let investments = []


// Deletes to do
function removeInvestment(idToDelete) {
    // if filter create copy of array. Need to reassign. todo is string
    investments = investments.filter(investment => {
    //if id of this todo matches idToDelete return false and delete it otherwise leave it
        if (investment.id === idToDelete){
            return false
        } else {return true}
    })
}

 //controller
function addInvestment(){
    const name = document.getElementById("inv-name").value
    const account = document.getElementById("inv-account").value
    const amount = document.getElementById("inv-amount").value
    const duedate = document.getElementById('inv-date').value
    createInvestment(name,account,duedate,amount)
    investmentRender()
}

function deleteInvestment(event){
    const deleteButton = event.target;
    const idToDelete = deleteButton.id
    removeInvestment(idToDelete)
    investmentRender()
}


//creates to do
function createInvestment(Name,Account,Duedate, Amount){
    const id = ''+ new Date().getTime() 

    investments.push({name:Name,
    account: Account,
    incomeDate: Duedate,
    inAmount: Amount,
    id: id}) 
}

 // View
function investmentRender(){
    // reset list
    document.getElementById('investments-list').innerHTML = '' 

    investments.forEach(investment => {
        const element = document.createElement('div')

        element.innerText = investment.name + '  ----  ' + investment.account +'  ------  ' + investment.incomeDate + '-----'+ investment.inAmount

        // add delete button for each element
        const deleteButton = document.createElement('button')
        deleteButton.innerText = 'Delete'
        deleteButton.style = 'margin-left: 16px'
        deleteButton.onclick = deleteInvestment
        deleteButton.id = investment.id
        element.appendChild(deleteButton)
        
        const investmentlist = document.getElementById('investments-list')
        investmentlist.appendChild(element)
    });
} 
investmentRender()
// =================================================================================================

// Liabilities
let liabilities = []


// Deletes to do
function removeLiability(idToDelete) {
    // if filter create copy of array. Need to reassign. todo is string
    liabilities = liabilities.filter(liability => {
    //if id of this todo matches idToDelete return false and delete it otherwise leave it
        if (liability.id === idToDelete){
            return false
        } else {return true}
    })
}

 //controller
function addLiability(){
    const name = document.getElementById("lname").value
    const account = document.getElementById("laccount").value
    const amount = document.getElementById("lamount").value
    const duedate = document.getElementById('ldate').value
    createLiability(name,account,duedate,amount)
    liabilitiesRender()
}

function deleteLiability(event){
    const deleteButton = event.target;
    const idToDelete = deleteButton.id
    removeLiability(idToDelete)
    liabilitiesRender()
}


//creates to do
function createLiability(Name,Account,Duedate, Amount){
    const id = ''+ new Date().getTime() 

    liabilities.push({name:Name,
    account: Account,
    incomeDate: Duedate,
    inAmount: Amount,
    id: id}) 
}

 // View
function liabilitiesRender(){
    // reset list
    document.getElementById('liabilities-list').innerHTML = '' 

    liabilities.forEach(liability => {
        const element = document.createElement('div')

        element.innerText = liability.name + '  ----  ' + liability.account +'  ------  ' + liability.incomeDate + '-----'+ liability.inAmount

        // add delete button for each element
        const deleteButton = document.createElement('button')
        deleteButton.innerText = 'Delete'
        deleteButton.style = 'margin-left: 16px'
        deleteButton.onclick = deleteLiability
        deleteButton.id = liability.id
        element.appendChild(deleteButton)
        
        const liabilitylist = document.getElementById('liabilities-list')
        liabilitylist.appendChild(element)
    });
} 
liabilitiesRender()
// =================================================================================================

