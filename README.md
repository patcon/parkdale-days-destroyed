# Parkdale Days Destroyed

_This project is asprational and is not year functional._

This is an experiment to borrow a concept from Bitcoin-land,
a measure called _Bitcoin days destroyed_ (BTCdd), and try to
apply it to the realm of gentrification as a rough indicator.

## Usage

```
mkvirtualenv parkdaledd --python=`which python3`
pip install -r requirements.txt
workon parkdaledd
python manage.py migrate
```

## Background

Generally, BTCdd were put forward as a way to guage economic activity in
the Bitcoin ecosystem. Bitcoin has an interested property for a monetary
system where every movement from one account to another happens in a
public ledger. The catch is that someone can inflate a simple view of
economic activity by moving money (quickly and cheaply) back and
forth between accounts. This might appear like economic activity, but
it's not "real".
So the clever idea was the weight the transfer by how
long it had previously been "at rest". The "days destroyed" are the
cumulative days at rest that are disrupted.
So 1 BTC moving from one
account to another after 1 year of sitting in that first account, would
be 365 BTCdd.

This measure particularly seemed to scratch an itch for bitcoiners, as there was
concern over hoarding of funds, and a sense that
"unsticking" Bitcoin that had long been at rest was a positive sign for the ecosystem.

In general, the reasons BTCdd could be calculated (and seemed _worth_
calculating) was because of a couple features of the Bitcoin ecosystem:

* **transferrable assets** in
* a **public ledger**
* for which the assets' **history at rest has meaning**


In reality, it [proved to be _not_ such a great indicator][] of economic
activity, and so it has rightfully fallen out of favour.

So then who cares?

The thought is that the above criteria hold true for businesses holding
space in buildings -- there's a transferrable asset (property) in a
public ledger (business license registry) for which the asset history
has meaning (long-term businesses have more community ties).

My hypothesis is that Parkdale business days destroyed (bdd) might be a
useful indicator in our toolkit. a 20-year-old business moving out of a
building (ie. 7,300 Parkdale bdd) would confer different meaning that a
two-year-old business moving out (730 Parkdale bdd). Of course there are
no solid conclusions to draw. A long-standing payday loan business might
be less great for the community than a two-year-old nepalese restaurant.
But the measure might help people better undestand the changes in
business landscape that precede the changes in tenant landscape and
housing costs that accompany gentrification.

Questions we might care to ask:

* What is the year-over-year trend in total Parkdale bdd for restaurants
  during the springtime (Mar 20 - June 20)?
* For all businesses in 2016, how many Parkdale bdd were there in North Parkdale
  vs South Parkdale (weighted by business license counts)?
* What are the total Parkdale bdd for each forward sortation area
  (weighted by business license counts), colour-coded on a map?

The answers to these question would give a sort of rough proxy for how
much business "roots" Parkdale might be losing. Since the city
continuously collects and releases business license data, it would be
fairly realtime, and no cost to collect.
